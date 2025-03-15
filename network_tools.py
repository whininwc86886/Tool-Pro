import geoip2.database
import socketio
from ipaddress import ip_address
from typing import Dict
from typing import Dict, Any

class NetworkTools:
    # ... 保留原有方法 ...

    @staticmethod
    def ip_geolocation(ip: str) -> Dict:
        """IP地址地理位置查询"""
        try:
            ip_address(ip)  # 验证IP有效性
            with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
                response = reader.city(ip)
                return {
                    '国家': response.country.name,
                    '城市': response.city.name,
                    '经纬度': (response.location.latitude, response.location.longitude),
                    '时区': response.location.time_zone
                }
        except Exception as e:
            return {'错误': str(e)}

    def start_http_server(self, port=8000):
        """启动简易HTTP服务器"""
        import http.server
        import socketserver
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Serving at port {port}")
            httpd.serve_forever()