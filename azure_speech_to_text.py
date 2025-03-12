import azure.cognitiveservices.speech as speechsdk

def convert_audio_to_text(audio_file):
    # 设置 Azure 语音服务的订阅密钥和区域
    subscription_key = "YOUR_AZURE_SPEECH_KEY"  # 替换为您的 API 密钥
    region = "YOUR_AZURE_REGION"  # 替换为您的区域（例如：eastus）

    # 创建语音配置
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)

    # 创建音频配置
    audio_input = speechsdk.AudioConfig(filename=audio_file)

    # 创建语音识别器
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    # 开始识别
    print("正在识别...")
    result = speech_recognizer.recognize_once()

    # 检查结果
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("识别结果: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("未识别到语音。")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("识别被取消: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("错误详情: {}".format(cancellation_details.error_details))

if __name__ == "__main__":
    audio_file = input("请输入音频文件路径：")
    convert_audio_to_text(audio_file)

