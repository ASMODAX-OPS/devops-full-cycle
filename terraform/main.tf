terraform {
  required_providers {
    minikube = {
      source = "scott-the-programmer/minikube"
    }
    kubernetes = {
      source = "hashicorp/kubernetes"
    }
  }
}

provider "minikube" {}

resource "minikube_cluster" "lab" {
  driver       = "docker"
  cluster_name = "devops-lab"
  cpus         = 4
  memory       = "4096mb"
  addons       = ["default-storageclass", "storage-provisioner", "metrics-server"]
}

provider "kubernetes" {
  host                   = minikube_cluster.lab.host
  client_certificate     = minikube_cluster.lab.client_certificate
  client_key             = minikube_cluster.lab.client_key
  cluster_ca_certificate = minikube_cluster.lab.cluster_ca_certificate
}

resource "kubernetes_namespace_v1" "app" {
  metadata {
    name = "app"
  }
}

resource "kubernetes_namespace_v1" "monitoring" {
  metadata {
    name = "monitoring"
  }
}