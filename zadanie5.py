"""Grayscale Image Conversion Comparison (CPU vs. GPU)
Copyright 2023 Dominika Bemberakova.
Licensed to MIT https://spdx.org/licenses/MIT.html

This module implements a script that converts color images to grayscale using both CPU and GPU processing.
"""


from numba import cuda
from PIL import Image
import numpy as np
import time


@cuda.jit
def cuda_calculate(image_in, image_out):
    """
    CUDA kernel that calculates the grayscale value for each pixel in the input image and stores it in the output image.

    Args:
        image_in: A numpy array representing the input image.
        image_out: A numpy array representing the output image.

    Returns:
        None.
    """
    x, y = cuda.grid(2)

    if x < image_in.shape[0] and y < image_in.shape[1]:
        r, g, b = image_in[x, y]
        gray_value = 0.2989 * r + 0.5870 * g + 0.1140 * b
        image_out[x, y] = gray_value


def grayscale_on_cpu(image):
    """
    Converts the input image to grayscale using CPU processing.

    Args:
        image: A PIL.Image object representing the input image.

    Returns:
        A numpy array representing the grayscale version of the input image.
    """
    image_in = np.array(image)
    image_out = np.empty((image_in.shape[0], image_in.shape[1]), dtype=np.uint8)

    for i in range(image_in.shape[0]):
        for j in range(image_in.shape[1]):
            r, g, b = image_in[i, j]
            gray_value = 0.2989 * r + 0.5870 * g + 0.1140 * b
            image_out[i, j] = gray_value

    return image_out


def grayscale_on_gpu(image):
    """
    Converts the input image to grayscale using GPU processing.

    Args:
        image: A PIL.Image object representing the input image.

    Returns:
        A numpy array representing the grayscale version of the input image.
    """
    # Allocate memory on GPU for the input and output images
    image_in = cuda.to_device(np.array(image))
    image_out = cuda.device_array((new_height, new_width), dtype=np.uint8)

    threadsperblock = (32, 32)
    blockspergrid_x = (image_in.shape[0] + threadsperblock[0] - 1) // threadsperblock[0]
    blockspergrid_y = (image_in.shape[1] + threadsperblock[1] - 1) // threadsperblock[1]
    blockspergrid = (blockspergrid_x, blockspergrid_y)

    cuda_calculate[blockspergrid, threadsperblock](image_in, image_out)
    # Copy the output image from GPU to CPU and return it
    return image_out.copy_to_host()


if __name__ == '__main__':
    # Check Cuda availability
    # print(cuda.is_available())

    input_image = Image.open("img3.jpg")
    # Define the desired resolution
    new_width = 270
    new_height = 350

    resized_image = input_image.resize((new_width, new_height))  # Resize the image

    start_gpu_time = time.time()  # Start the timer for GPU
    output_gpu = grayscale_on_gpu(resized_image)  # Convert the image to grayscale by using GPU
    output_gpu = Image.fromarray(output_gpu)
    output_gpu.save("output3_gpu.jpg")  # Save the grayscale image to a file
    elapsed_gpu_time = time.time() - start_gpu_time  # Calculate the elapsed time for GPU

    start_cpu_time = time.time()  # Start the timer for CPU
    output_cpu = grayscale_on_cpu(resized_image)  # Convert the image to grayscale by using CPU
    output_cpu = Image.fromarray(output_cpu)
    output_cpu.save("output3_cpu.jpg")  # Save the grayscale image to a file
    elapsed_cpu_time = time.time() - start_cpu_time  # Calculate the elapsed time for CPU

    print(f"Grayscale image3 saved successfully! GPU Time elapsed: {elapsed_gpu_time:.4f} seconds")
    print(f"Grayscale image3 saved successfully! CPU Time elapsed: {elapsed_cpu_time:.4f} seconds")

    # Display the input and output images
    resized_image.show()
    output_gpu.show()
