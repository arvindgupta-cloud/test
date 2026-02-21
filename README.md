# 🚀 End-to-End: Deploy Flask App to GKE using Artifact Registry

## 📌 1️⃣ Enable Required APIs

```bash
gcloud services enable \
container.googleapis.com \
artifactregistry.googleapis.com \
cloudbuild.googleapis.com \
run.googleapis.com
```

## 📌 2️⃣ Create Artifact Registry Repository

```bash
gcloud artifacts repositories create my-repo \
  --repository-format=docker \
  --location=asia-south1 \
  --description="Docker repo for GKE apps"
```

## 📌 3️⃣ Build & Push Image Using Cloud Build

```bash
gcloud builds submit \
  --tag asia-south1-docker.pkg.dev/YOUR_PROJECT_ID/my-repo/my-app:v1
```

## 📌 4️⃣ Create GKE Cluster

```bash
gcloud container clusters create my-gke-cluster \
  --zone asia-south1-a \
  --num-nodes 2
```

Optional Get credentials:

```bash
gcloud container clusters get-credentials my-gke-cluster \
  --zone asia-south1-a
```

## 📌 5️⃣ Create Deployment YAML

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: asia-south1-docker.pkg.dev/YOUR_PROJECT_ID/my-repo/my-app:v1
        ports:
        - containerPort: 8080
```

**Apply:**

```bash
kubectl apply -f deployment.yaml
```

## 📌 6️⃣ Create Service (ClusterIP)

```bash
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: ClusterIP
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
```

**Apply:**

```bash
kubectl apply -f service.yaml
```

## 📌 7️⃣ Create Ingress

```bash
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app-ingress
spec:
  ingressClassName: gce
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              number: 80
```

**Apply:**

```bash
kubectl apply -f ingress.yaml
```

## 📌 8️⃣ Get External IP

```bash
kubectl get ingress
```

Wait 2–5 minutes until you see:

```bash
ADDRESS: 34.xx.xx.xx
```

Access:

```bash
http://EXTERNAL-IP
http://EXTERNAL-IP/about
http://EXTERNAL-IP/contact
http://EXTERNAL-IP/shop
```
