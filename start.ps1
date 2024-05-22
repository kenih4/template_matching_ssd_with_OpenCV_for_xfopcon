#requires -version 2.0

param( 
    [string]$email = "test", 
    [string]$password = "test" 
) 

#."include\Get-FolderItem.ps1"
Add-Type -AssemblyName "System.Web" 
Add-Type -AssemblyName "System.Windows.Forms" 
Add-Type -AssemblyName "System.Drawing" 

#        [System.Windows.Forms.MessageBox]::Show("START", "Wargning")


$hos = [System.Net.Dns]::GetHostName()
#[System.Windows.Forms.MessageBox]::Show( $hos , "Wargning")
#  LAPTOP-9H6C2Q7O
#  LAPTOP-H9B24TO9


#start-transcript console.txt -append
#start-transcript -path C:\me\daq_FB\transcript.log
start-transcript -path transcript.log

$timer = New-Object Windows.Forms.Timer 
$timer.Interval =  600000 #7200000 #3600000  #usec
$trayTitle = "template_matching" 

 
$menuItem1 = New-Object Windows.Forms.MenuItem "終了(&X)" 
$menuItem1.Add_Click( 
{ 
    $notifyIcon.Visible = $false 
    $notifyIcon.Dispose() 
    [Windows.Forms.Application]::Exit() 
})  
$contextMenu = New-Object Windows.Forms.ContextMenu   
[void]$contextMenu.MenuItems.Add($menuItem1)
 
$notifyIcon = New-Object Windows.Forms.NotifyIcon 
#$notifyIcon.Icon = [Drawing.Icon]::ExtractAssociatedIcon("$pshome\powershell.exe") 
$notifyIcon.Icon = "kaede.ico" #"pen.ico"
$notifyIcon.Visible = $true 

$notifyIcon.ContextMenu = $contextMenu 
$notifyIcon.Add_MouseDoubleClick( 
{ 
    Start-Process "C:\me\template_matching_ssd_with_OpenCV_for_xfopcon"
}) 
$notifyIcon.Add_BalloonTipClicked( 
{
})


$action =  
{

#    $newdt = (Get-Date).AddSeconds(-60)

#    [string[]]$array1 = @("SACLA",(Get-Date).Year,(Get-Date).Month,(Get-Date).Day,(Get-Date).Hour,(Get-Date).Minute)
#    Write-Host $array1
#    Start-Process -FilePath C:\me\daq_FB\daq_FB.exe -ArgumentList $array1 -Wait -NoNewWindow

#    [string[]]$array2 = @("SCSS",(Get-Date).Year,(Get-Date).Month,(Get-Date).Day,(Get-Date).Hour,(Get-Date).Minute)
#    Write-Host $array2
#    Start-Process -FilePath C:\me\daq_FB\daq_FB.exe -ArgumentList $array2 -Wait -NoNewWindow


#python template_matching_ssd_with_OpenCV_for_xfopcon.py xfopcon-09.png xfopcon-09_cathodeFB.png xfopcon-09_chopperFB.png xfopcon-09_alarmvoice.png

# SCSS+
    [string[]]$array1 = @("C:\me\template_matching_ssd_with_OpenCV_for_xfopcon\template_matching_ssd_with_OpenCV_for_xfopcon.py", "xfopcon-09.png", "xfopcon-09_cathodeFB.png", "xfopcon-09_chopperFB.png", "xfopcon-09_alarmvoice.png")
    Write-Host $array1
    Start-Process -FilePath python -ArgumentList $array1 -Wait -NoNewWindow
# SACLA xfopcon-04
    [string[]]$array2 = @("C:\me\template_matching_ssd_with_OpenCV_for_xfopcon\template_matching_ssd_with_OpenCV_for_xfopcon.py", "xfopcon-04.png", "xfopcon-04_cathodeFB.png", "xfopcon-04_chopperFB.png", "xfopcon-04_unitchange.png")
    Write-Host $array2
    Start-Process -FilePath python -ArgumentList $array2 -Wait -NoNewWindow

}
 
$timer.Add_Tick($action) 
$timer.Enabled = $true 
$timer.Start() 
[Windows.Forms.Application]::Run()


#
#    Start-Process -FilePath C:\me\daq_FB\daq_FB.exe "SACLA 2019 3 1 8 0"
#    Start-Process -FilePath C:\me\daq_FB\daq_FB.exe -ArgumentList SACLA,2019,3,1,8,0
#



