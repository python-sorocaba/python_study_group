# -*- coding: utf-8 -*-
import os
import unittest
from unittest.mock import patch

import diary


class TestDiary(unittest.TestCase):
    def setUp(self):
        # Create structure.json file
        keys = ['nome', 'dia', 'compromisso']
        self.create_basic_structure(keys)

    def create_basic_structure(self, keys):
        """
        This function fake my input function on
        diary.create_structure function and create basic
        structure on structure.json file
        """
        with patch.object(diary, 'input', return_value=None) as my_diary_input:
            # option c cancel iteration of for loop
            # on create_structure function
            my_diary_input.side_effect = keys + ['c']
            return diary.create_structure()

    def create_basic_task(self, task, structure):
        """
        This function fake my input function on
        diary.write_task function and create basic
        task on tasks.json file
        """
        with patch.object(diary, 'input', return_value=None) as my_diary_input:
            my_diary_input.side_effect = task
            return diary.write_task(structure)

    @patch('diary.input')
    def test_create_structure_basic(self, mock_input):
        mock_input.return_value = None
        mock_input.side_effect = ['teste', 'c']
        diary.create_structure()
        self.assertTrue(os.path.isfile('structure.json'))

    def test_create_structure(self):
        """Test if create_structure generate structure.json file"""
        self.assertTrue(os.path.isfile('structure.json'))

    def test_read_structure(self):
        """Test if generated file by create structure is ok"""
        structure = diary.read_structure()
        expected_dict = {"nome": None, "compromisso": None, "dia": None}
        self.assertEqual(structure, expected_dict)

    def test_write_task(self):
        """Test if write new task on structure is ok"""
        structure = diary.read_structure()
        task = ['rafael', '21/04/2016', 'terminar o exercicio']
        self.create_basic_task(task, structure)
        self.assertTrue(os.path.isfile('tasks.json'))

    def test_read_tasks(self):
        """Test if generated file by write tasks is ok"""
        # get an structure
        structure = diary.read_structure()

        # create two tasks
        tasks = (
            ['terminar o exercicio', '21/04/2016', 'rafael'],
            ['trabalhar', '22/04/2016', 'rafael']
        )
        self.create_basic_task(tasks[0], structure)
        self.create_basic_task(tasks[1], structure)

        # read tasks created
        tasks = diary.read_tasks()
        expected_tasks = [
            {
                'nome': 'rafael',
                'dia': '21/04/2016',
                'compromisso': 'terminar o exercicio'
            },
            {
                'nome': 'rafael',
                'dia': '22/04/2016',
                'compromisso': 'trabalhar'
            }
        ]
        # verify if expected task in tasks created
        for expected_task in expected_tasks:
            self.assertIn(expected_task, tasks)

    def test_show_tasks(self):
        """Test show_tasks"""
        import sys
        from io import StringIO
        tasks = [
            {
                'nome': 'rafael',
                'dia': '21/04/2016',
                'compromisso': 'terminar o exercicio'
            },
            {
                'nome': 'rafaelXYZ',
                'dia': '22/04/2016',
                'compromisso': 'trabalhar'
            }
        ]
        saved_stdout = sys.stdout
        try:
            fake_out = StringIO()
            sys.stdout = fake_out
            diary.show_tasks(tasks)
            output = fake_out.getvalue().strip()
            self.assertIn('dia: 21/04/2016', output)
            self.assertIn('dia: 22/04/2016', output)
            self.assertIn('compromisso: terminar o exercicio', output)
            self.assertIn('compromisso: trabalhar', output)
            self.assertIn('nome: rafael', output)
            self.assertIn('nome: rafaelXYZ', output)
        finally:
            sys.stdout = saved_stdout

    def tearDown(self):
        """Remove files created on tests"""
        if os.path.isfile('structure.json'):
            os.remove('structure.json')

        if os.path.isfile('tasks.json'):
            os.remove('tasks.json')
