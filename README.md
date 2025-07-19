
# 🛒 Flipkart Product Recommender System

This is an end-to-end Generative AI-based product recommender system that suggests Flipkart products using LLMs and embeddings. The system leverages LangChain to interact with LLMs, uses Hugging Face models for embeddings, stores vectors in AstraDB, and is deployed on a GCP VM using Kubernetes with real-time monitoring via Prometheus and Grafana.

---

## 🔍 Project Objective

To build a scalable, cloud-deployable recommendation system that:
- Uses LLMs to understand user queries.
- Converts product descriptions into vector embeddings.
- Recommends top-matching products based on semantic similarity.
- Visualizes system health and metrics using Prometheus and Grafana.

---

## 🧱 Project Components

### 1. **Local Project Setup**
- `Project and API Setup`: Environment setup and API keys configuration.
- `Configuration Code`: Manages API and model parameters.
- `Data Converter Code`: Preprocess and chunk product data.
- `Data Ingestion Code`: Embedding creation and vector storage in AstraDB.
- `RAG Chain Code`: Implements Retrieval-Augmented Generation using LangChain.
- `Application Code`: Flask backend with HTML/CSS frontend.

### 2. **Containerization and Orchestration**
- `Dockerfile`: Creates Docker image for the app.
- `Kubernetes Deployment`: YAML file to deploy app into a cluster using Minikube inside a GCP VM.

### 3. **Monitoring Setup**
- `Prometheus`: Scrapes metrics from the deployed app.
- `Grafana`: Visualizes those metrics through interactive dashboards.

### 4. **Version Control**
- `GitHub`: Source code versioning and collaboration.

### 5. **Cloud Deployment**
- `GCP VM`: A virtual machine on Google Cloud Platform.
- `Minikube`: Sets up a single-node Kubernetes cluster inside the VM.
- `kubectl`: CLI to deploy and manage the Kubernetes workloads.

---

## 🔗 Flow Architecture

1. User queries product recommendations via frontend.
2. Flask backend sends query to LangChain → Groq LLM.
3. Embeddings generated via Hugging Face.
4. Vector comparison performed with AstraDB.
5. Result is returned to frontend.
6. Dockerized app is deployed via Kubernetes in GCP VM.
7. Prometheus scrapes metrics like request count, latency, memory usage.
8. Grafana visualizes metrics with real-time dashboards.

---

## ⚙️ Tech Stack

| Category              | Tool/Tech                       |
|-----------------------|---------------------------------|
| LLM                   | Groq 3.3                        |
| Embedding Model       | Hugging Face Transformers       |
| Vector Store          | Astra DB                        |
| AI Framework          | LangChain                       |
| Backend               | Flask                           |
| Frontend              | HTML, CSS                       |
| Containerization      | Docker                          |
| Orchestration         | Kubernetes via Minikube         |
| Cloud Provider        | GCP VM                          |
| Monitoring            | Prometheus, Grafana             |
| CLI                   | kubectl                         |
| Version Control       | GitHub                          |

---

## 📦 Monitoring Workflow

- **Prometheus** scrapes metrics exposed at `/metrics` endpoint by Flask app.
- **Grafana** queries Prometheus and visualizes:
  - API latency
  - Request count
  - CPU and memory usage
  - Custom user-defined metrics

---


































Tech Stack:

1.Groq --> LLM 3.3

2. HuggingFace --> Embedding Model[Doc --> Chunks embedding  -->  Vector Database storing]

3.GCP VM --> To deploy and run your app on the cloud within a virtual machine. Its a service offered by google cloud(Renting a computer to run our project).

4.Langchain -- > Generative AI Framework to interact with LLM(Interact with LLM).

5.Minikube --> Making a kuberntes Cluster inside a VM(Deployment in kuberntes cluster using minikube)

6.Docker --> For containerization of the app during deployment(Deployment container).

7. Flask --> Formaking backedn of your application(Backend).

8. HTML/CSS --> To make UI or fronted of the app(Front End).

9. Kubectl --> CLI tool for Kuberntes to interact with minikube.

10. Github --> it will work as Source Code Management for your project.

11. AstraDB --> Work as vector store(Online Vector store).

12. Prometheus --> Collects and stores real time metrics (like cpu usage, memory, request dne, monitoring) from your application running in kubernetes. we can also make custom metrics.

13. Grafana --> Visualizes those metrics in form of beautiful visalizes.



![alt text](image.png)




![alt text](image-1.png)





