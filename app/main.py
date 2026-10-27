from fastapi import FastAPI, HTTPException
from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

app = FastAPI(title="ClusterPulse", version="0.1.0")


def get_k8s_client():
    try:
        config.load_incluster_config()
    except ConfigException:
        config.load_kube_config()

    return client.CoreV1Api()


@app.get("/health")
def health():
    return {"status": "healthy", "service": "clusterpulse"}


@app.get("/api/nodes")
def nodes():
    try:
        api = get_k8s_client()
        result = api.list_node()

        return [
            {
                "name": node.metadata.name,
                "conditions": [
                    {
                        "type": c.type,
                        "status": c.status
                    }
                    for c in node.status.conditions
                ]
            }
            for node in result.items
        ]
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc))


@app.get("/api/pods")
def pods():
    try:
        api = get_k8s_client()
        result = api.list_pod_for_all_namespaces()

        return [
            {
                "name": pod.metadata.name,
                "namespace": pod.metadata.namespace,
                "phase": pod.status.phase
            }
            for pod in result.items
        ]
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc))
