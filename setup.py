from setuptools import setup, find_packages


def get_requirements(file_path:str)->list[str]:
    '''
    input: file name (text file)
    output: list of requirements in text file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", " ") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='M5_forcasting',
    version= '0.0.1',
    author='Khoa Tran',
    author_email= 'dinhdangkhoatran2005@gmail.com',
    install_requires= get_requirements('requirements.txt'),
    packages= find_packages(),
)