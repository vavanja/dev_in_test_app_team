def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'deviceName': 'emulator-5554',
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        # 'takesScreenshot': True,
        # 'udid': '11bd127d',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }

# 'automationName': 'uiautomator2',
# 'deviceName': 'emulator-5554',
# 'platformName': 'Android',
# 'platformVersion': '10',
# 'resetKeyboard': True,
# 'appPackage': 'com.ajaxsystems',
# 'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
