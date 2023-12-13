import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torchvision.models import inception_v3
from scipy.linalg import sqrtm
import numpy as np


import os
import glob
from PIL import Image

def calculate_activation_statistics(images, model, batch_size=50, dims=2048):
    model.eval()
    n_batches = len(images) // batch_size
    act = np.empty((len(images), dims))

    for i in range(n_batches):
        start = i * batch_size
        end = (i + 1) * batch_size
        batch = images[start:end].cuda()
        print(batch.shape)
        pred = model(batch)
        pred = pred[0].squeeze(2).squeeze(2).cpu().data.numpy()
        act[start:end] = pred

    mu = np.mean(act, axis=0)
    sigma = np.cov(act, rowvar=False)
    return mu, sigma

def calculate_frechet_distance(mu1, sigma1, mu2, sigma2):
    eps = 1e-6
    sqrt_term = sqrtm(sigma1.dot(sigma2))
    if np.iscomplexobj(sqrt_term):
        sqrt_term = sqrt_term.real
    fid = np.sum((mu1 - mu2)**2) + np.trace(sigma1 + sigma2 - 2*sqrt_term)
    return fid

def preprocess_images(images):
    transform = transforms.Compose([
        transforms.Resize((299, 299)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return torch.stack([transform(image) for image in images])

def calculate_fid_score(real_images, generated_images, batch_size=50):
    # real_images = preprocess_images(real_images)
    # generated_images = preprocess_images(generated_images)

    model = inception_v3(pretrained=True, transform_input=False).cuda()
    model = nn.Sequential(*list(model.children())[:-2])  # Remove the last two layers

    mu_real, sigma_real = calculate_activation_statistics(real_images, model, batch_size)
    mu_fake, sigma_fake = calculate_activation_statistics(generated_images, model, batch_size)

    fid_score = calculate_frechet_distance(mu_real, sigma_real, mu_fake, sigma_fake)
    return fid_score



def load_images_from_directory(directory_path):
    image_list = []

    # Define a transformation to preprocess the images
    transform = transforms.Compose([
        transforms.Resize((299, 299)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    for filename in os.listdir(directory_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(directory_path, filename)
            image = Image.open(file_path).convert("RGB")
            image = transform(image)
            image_list.append(image)

    # Stack the images into a single tensor
    images_tensor = torch.stack(image_list)

    return images_tensor

if __name__=="__main__":
    # Define your directories for real and synthetic images
    real_images_directory = "/home/aru/yolov5_hdr/datasets/80_real/fold1/images/train"
    synthetic_images_directory = "/home/aru/yolov5_hdr/datasets/80_real/fold2/images/train"

    # Load real and synthetic images
    real_images = load_images_from_directory(real_images_directory)
    generated_images = load_images_from_directory(synthetic_images_directory)

    # Example usage:
    # real_images and generated_images should be PyTorch tensors with shape (num_samples, channels, height, width)
    fid = calculate_fid_score(real_images, generated_images)
    print(f"FID Score: {fid}")



