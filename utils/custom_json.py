# project_root/renderers/custom_json.py

from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response') if renderer_context else None
        original_status = response.status_code if response else 0

        # 强制所有响应使用 200 HTTP 状态码
        if response:
            response.status_code = 200

        if response and response.exception:
            wrapper = {
                'code': original_status,  # 保留原始错误码
                'message': data.get('detail', '服务器异常' if original_status == 500 else 'error'),
                'data': None
            }
        else:
            wrapper = {
                'code': original_status,
                'message': 'success',
                'data': data
            }

        return super().render(wrapper, accepted_media_type, renderer_context)
