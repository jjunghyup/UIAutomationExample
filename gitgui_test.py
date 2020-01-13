
def test_gitgui():
    # Clone폴더 값 정의
    clone_folder = "C:\\dev\\git\\UIAutomationExample"
    # Clone 대상 폴더가 존재할 경우 폴더를 지운다.
    import os
    if os.path.exists(clone_folder):
        os.system('rmdir /S /Q "{}"'.format(clone_folder))

    # Clone 대상 폴더가 없는지 확인한다.
    if os.path.exists(clone_folder):
        assert False, "clone대상폴더가 지워지지 않음"

    # GIT GUI를 실행시킨다.
    import uiautomation as auto
    # 검색영역 클릭하기
    auto.ButtonControl(searchDepth=3, Name='검색하려면 여기에 입력하십시오.').Click()
    # 검색영역에 값 입력하기
    auto.EditControl(searchDepth=3, Name='검색 상자').SendKeys('git gui')
    # Git GUI아이콘 클릭하기
    auto.TextControl(searchDepth=10, Name="Git GUI").Click()
    # 프로그램이 정상적으로 수행되었는지 확인한다.
    auto.WindowControl(searchDepth=1,  Name="Git Gui")

    # 상단 메뉴를 통해 Clone을 수행
    auto.MenuItemControl(searchDepth=8,  Name="Repository").Click()
    auto.MenuItemControl(searchDepth=8, Name="Repository")
    # inspect를 통해서 menu의 AutomationId가 48이므로 이를 활용
    auto.MenuItemControl(AutomationId = "48").Click()
    # 화면이 Clone Existing Repository 세부설정화면으로 이동되었는지 확인한다.
    # 아쉽게도 해당 APP은 "Clone Existing Repository"에 대한 정보를 확인할 수 없는 앱이어서
    # 이후 동작으로 확인할 수 밖에 없다.

    # Source location 및 Target Directory 값 정의
    source_location = "https://github.com/jjunghyup/UIAutomationExample.git"
    target_directory = "C:\\dev\\git\\UIAutomationExample"
    # Source Location값과 Target Directory값을 입력한다.
    auto.PaneControl(ClassName="TkChild", foundIndex=14).Click()
    auto.PaneControl(ClassName="TkChild", foundIndex=14).SendKeys(source_location)
    auto.PaneControl(ClassName="TkChild", foundIndex=11).Click()
    auto.PaneControl(ClassName="TkChild", foundIndex=11).SendKeys(target_directory)
    # 값이 정상적으로 입력된다.
    # 값을 Clipboard에 복사하고 붙여넣기 식으로 확인이 가능하지만 해당 내용은 이후에 작성 예정

    # Clone 버튼을 클릭한다.
    auto.PaneControl(ClassName="TkChild", foundIndex=18).Click()
    # Clone 대상폴더가 존재하는지 확인한다. 10초 동안 확인한다.
    result = False
    for i in range(0, 10):
        if os.path.exists(clone_folder):
           result = True

    assert result, "clone대상폴더가 존재 하지 않음"


