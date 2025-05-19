# project_root/renderers/custom_json.py

from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    """
    把 DRF 所有输出都包装成：
    {
        "code": <HTTP 状态码>,
        "message": "<状态文本或自定义>",
        "data": <原始 data>
    }
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response', None)
        # 如果视图直接返回了错误，DRF 会把 data 放到 'detail' 键
        if response is not None and response.exception:
            wrapper = {
                'code': response.status_code,
                'message': data.get('detail', 'error'),
                'data': None
            }
        else:
            wrapper = {
                'code': response.status_code if response else 0,
                'message': 'success',
                'data': data
            }

        return super().render(wrapper, accepted_media_type, renderer_context)
