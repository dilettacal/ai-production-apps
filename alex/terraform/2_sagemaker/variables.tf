variable "aws_region" {
  description = "AWS region for resources"
  type        = string
}

variable "sagemaker_image_tag" {
  description = "Tag/version of the SageMaker HuggingFace container image"
  type        = string
  default     = "1.13.1-transformers4.26.0-cpu-py39-ubuntu20.04"
}

variable "embedding_model_name" {
  description = "Name of the HuggingFace model to use"
  type        = string
  default     = "sentence-transformers/all-MiniLM-L6-v2"
}