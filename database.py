from typing import Optional
import redis, json

RedisClient = redis.Redis(
    host = "localhost",
    port = 6379,
    decode_responses = True
)

def CreateJob(jobId: str, filename: str):
    jobData = {
        "status": "queued",
        "filename": filename,
        "result": None,
        "error": None
    }

    RedisClient.setex(
        f"job:{jobId}",
        3600,
        json.dumps(jobData)
    )

    return jobData

def GetJob(jobId: str) -> Optional[dict]:
    data = RedisClient.get(f"job:{jobId}")

    return json.loads(data) if data else None

def UpdateJob(jobId: str, status: str = None, result: dict = None, error: str = None):
    job = GetJob(jobId)

    if not job:
        return None

    if status:
        job["status"] = status
    if result:
        job["result"] = result
    if error:
        job["error"] = error
    
    RedisClient.setex(
        f"job:{jobId}",
        3600,
        json.dumps(job)
    )

    return job