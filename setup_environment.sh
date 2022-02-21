if [ ! -d venv ]
then
    echo 'Setting up virtualenv...'
    virtualenv venv
fi
source venv/bin/activate
echo 'Installing python dependencies...'
pip install -r requirements.txt
echo 'Done!'