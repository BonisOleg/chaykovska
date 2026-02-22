from django.test import TestCase
from ..models import MosaicCell, AboutSection, ContactInfo


class MosaicCellTest(TestCase):
    def setUp(self):
        self.cell = MosaicCell.objects.create(
            position=1,
            size_type='half'
        )
    
    def test_mosaic_cell_creation(self):
        self.assertEqual(self.cell.position, 1)
        self.assertTrue(self.cell.is_active)


class AboutSectionTest(TestCase):
    def setUp(self):
        self.section = AboutSection.objects.create(
            section_type='brand',
            title='Our Brand',
            content='Brand content here'
        )
    
    def test_about_section_creation(self):
        self.assertEqual(self.section.section_type, 'brand')
        self.assertEqual(self.section.title, 'Our Brand')
