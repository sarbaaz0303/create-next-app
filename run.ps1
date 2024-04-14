pip install wheel requests

python setup.py sdist bdist_wheel
pip install -e . 

If (Test-Path -Path 'test-project') {
    Remove-Item -Path 'test-project' -Recurse
}
Write-Host "`n`n"

python -m create-next-app test-project