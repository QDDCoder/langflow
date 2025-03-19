# from langflow.field_typing import Data
from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema import Data


class PensionPolicy(Component):
    display_name = "养老金政策"
    description = "养老金政策"
    documentation: str = "https://docs.langflow.org/components-custom-components"
    icon = "code"
    name = "PensionPolicy"

    inputs = [
        MessageTextInput(
            name="input_value",
            display_name="Input Value",
            info="这是一个测试输入",
            value="请输入你的问题",
            tool_mode=False,
        ),
    ]

    outputs = [
        Output(display_name="Output", name="output", method="build_output"),
    ]

    def build_output(self) -> Data:
        data = Data(value=self.input_value)
        self.status = data
        return data
