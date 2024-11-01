import requests
import time

def test_endpoints():
    base_url = "http://localhost:8000"
    endpoints = [
        '/health',
        '/api/about',
        '/api/experience',
        '/api/skills',
        '/api/projects'
    ]
    
    results = []
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}")
            results.append({
                "endpoint": endpoint,
                "status": response.status_code,
                "response_time": response.elapsed.total_seconds(),
                "success": response.status_code == 200
            })
        except Exception as e:
            results.append({
                "endpoint": endpoint,
                "status": "Error",
                "error": str(e),
                "success": False
            })
    
    return results

if __name__ == "__main__":
    print("Testing production setup...")
    print("Make sure the server is running with Gunicorn first!")
    time.sleep(2)
    
    results = test_endpoints()
    
    print("\nTest Results:")
    print("-" * 50)
    for result in results:
        status = "✅" if result.get("success") else "❌"
        print(f"{status} {result['endpoint']}: {result.get('status')}")
        if not result.get("success"):
            print(f"   Error: {result.get('error', 'Unknown error')}")
        elif "response_time" in result:
            print(f"   Response time: {result['response_time']:.3f}s")
    print("-" * 50)