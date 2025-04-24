# India Historical Transformation Script (Bedrock + LLaMA 2 and AI21 J2 Mid)

This Python script uses AWS Bedrock with the `meta.llama2-70b-chat-v1` and `ai21.j2-mid-v1` model to generate a historical transformation narrative of India over the last 1000 years.

## Features

- Uses the powerful LLaMA 2 70B chat model and AI21 Labs' J2 Mid model via AWS Bedrock.
- Customizable prompt to explore historical or generative responses.
- Configurable parameters like max generation length, temperature, and top-p sampling.

## Requirements

- Python 3.8+
- Boto3
- AWS credentials with access to Bedrock

## Installation

Install required dependencies:

```bash
pip install boto3
pip install awscli

## Configure your AWS credentials (e.g., via AWS CLI or environment variables):

- aws configure


## Image Generation 

# 🇮🇳 India's 1000-Year Transformation - 4K Image Generation with Stable Diffusion XL

This Python script generates a **4K HD AI-generated image** of India depicting its **dynamic transformation over the past 1000 years** using **Stable Diffusion XL** via **AWS Bedrock**.

## 📸 Features

- Prompts a generative AI model to create a historical-themed high-resolution image of India.
- Uses Stability AI's `stable-diffusion-xl-v0` model through AWS Bedrock.
- Saves the resulting image to your local filesystem.
- Fully automated image generation pipeline with configurable prompt, resolution, and steps.

-- output/generated-img.png

