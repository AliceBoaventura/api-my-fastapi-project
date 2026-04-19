from fastapi import FastAPI
from datetime import datetime
import pytz
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Digital Clock API", version="1.0.0")

class TimeZoneRequest(BaseModel):
    timezones: List[str] = ["UTC", "US/Eastern", "US/Pacific", "Europe/London", "Asia/Tokyo"]

class ClockResponse(BaseModel):
    timezone: str
    current_time: str
    unix_timestamp: int
    offset: str

@app.get("/")
async def root():
    return {
        "message": "Welcome to Digital Clock API",
        "endpoints": {
            "current_time": "/time",
            "all_timezones": "/time/all",
            "custom_timezones": "/time/custom (POST)"
        }
    }

@app.get("/time")
async def get_current_time(timezone: str = "UTC") -> ClockResponse:
    """Get current time in a specific timezone"""
    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        return ClockResponse(
            timezone=timezone,
            current_time=now.strftime("%Y-%m-%d %H:%M:%S %Z"),
            unix_timestamp=int(now.timestamp()),
            offset=now.strftime("%z")
        )
    except Exception as e:
        return {"error": f"Invalid timezone: {timezone}"}

@app.get("/time/all")
async def get_all_timezones() -> List[ClockResponse]:
    """Get current time in multiple default timezones"""
    timezones = ["UTC", "US/Eastern", "US/Pacific", "Europe/London", "Asia/Tokyo", "Australia/Sydney", "Asia/Dubai"]
    results = []
    
    for tz_name in timezones:
        try:
            tz = pytz.timezone(tz_name)
            now = datetime.now(tz)
            results.append(ClockResponse(
                timezone=tz_name,
                current_time=now.strftime("%Y-%m-%d %H:%M:%S %Z"),
                unix_timestamp=int(now.timestamp()),
                offset=now.strftime("%z")
            ))
        except Exception:
            pass
    
    return results

@app.post("/time/custom")
async def get_custom_timezones(request: TimeZoneRequest) -> List[ClockResponse]:
    """Get current time in custom timezones"""
    results = []
    
    for tz_name in request.timezones:
        try:
            tz = pytz.timezone(tz_name)
            now = datetime.now(tz)
            results.append(ClockResponse(
                timezone=tz_name,
                current_time=now.strftime("%Y-%m-%d %H:%M:%S %Z"),
                unix_timestamp=int(now.timestamp()),
                offset=now.strftime("%z")
            ))
        except Exception as e:
            results.append({"error": f"Invalid timezone: {tz_name}"})
    
    return results

@app.get("/timezones/list")
async def list_available_timezones() -> dict:
    """List all available timezones"""
    return {
        "count": len(pytz.all_timezones),
        "timezones": pytz.all_timezones
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)