import os
import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlumniManagement.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from alumni.models import (
    Alumni, GraduationYear, BatchMentor, AlumniCoordinator,
    Event, GalleryPhoto, VisitorCount
)

def seed():
    print("Seeding database with Parala Maharaja Engineering College data...")

    # 1. Graduation Years
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    year_objs = {}
    for y in years:
        obj, _ = GraduationYear.objects.get_or_create(year=y)
        year_objs[y] = obj
    print(f"Created/verified {len(years)} graduation years.")

    # 2. Coordinator
    coord, created = AlumniCoordinator.objects.get_or_create(
        email='coordinator@pmec.ac.in',
        defaults={
            'name': 'Prof. Dr. S. K. Mohapatra',
            'password': make_password('password123'),
            'mobile': '9876543210'
        }
    )
    if not created:
        coord.password = make_password('password123')
        coord.save()
    print("Coordinator seeded: coordinator@pmec.ac.in / password123")

    # 3. Batch Mentors
    mentor_photos = [
        'media/mentor_photos/dummy.jpeg',
        'media/mentor_photos/WhatsApp_Image_2025-04-21_at_13.52.00_3e81c6a4.jpg'
    ]

    mentor1, created = BatchMentor.objects.get_or_create(
        username='nkulkarni',
        defaults={
            'full_name': 'Prof. Dr. R. K. Mishra',
            'email': 'rkmishra@pmec.ac.in',
            'password': make_password('password123'),
            'mobile': '9822012345',
            'profile_photo': mentor_photos[0] if os.path.exists(os.path.join('static', 'media', mentor_photos[0])) else ''
        }
    )
    if not created:
        mentor1.password = make_password('password123')
        mentor1.save()
    mentor1.assigned_batches.set([year_objs[2021], year_objs[2022], year_objs[2023]])

    mentor2, created = BatchMentor.objects.get_or_create(
        username='ppatil',
        defaults={
            'full_name': 'Prof. Sunita Patnaik',
            'email': 'spatnaik@pmec.ac.in',
            'password': make_password('password123'),
            'mobile': '9822054321',
            'profile_photo': mentor_photos[1] if os.path.exists(os.path.join('static', 'media', mentor_photos[1])) else ''
        }
    )
    if not created:
        mentor2.password = make_password('password123')
        mentor2.save()
    mentor2.assigned_batches.set([year_objs[2024], year_objs[2025]])
    print("Mentors seeded: nkulkarni / password123, ppatil / password123")

    # 4. Alumni Records (with existing photos)
    profile_photos = [
        'media/profile_photos/Nedre_Dattatray.jpg',
        'media/profile_photos/1742477471185.jpg',
        'media/profile_photos/20250126_124749000_iOS.jpg',
        'media/profile_photos/DSC_0049.JPG',
        'media/profile_photos/IMG-20250131-WA0015.jpg',
        'media/profile_photos/IMG_20231212_194617.jpg',
        'media/profile_photos/IMG_20240926_191850.jpg',
        'media/profile_photos/IMG_20241023_210421.jpg',
        'media/profile_photos/IMG_20250302_202845_868.jpg',
        'media/profile_photos/IMG_20250404_213534.jpg'
    ]

    demo_alumni_data = [
        {
            'email': 'rahul.sharma@example.com',
            'full_name': 'Rahul Sharma',
            'mobile': '+91 9876543210',
            'current_job_profile': 'Staff Systems Architect',
            'current_company': 'Cisco Systems',
            'current_job_location': 'Bangalore, India',
            'city': 'Bangalore',
            'sub_district': 'Bangalore South',
            'district': 'Bangalore Urban',
            'state': 'Karnataka',
            'pincode': '560100',
            'is_international': False,
            'country': 'India',
            'full_address': 'Flat 402, Green Glen Layout, Bellandur, Bangalore',
            'graduation_year': 2018,
            'experience': 7,
            'sector': 'Telecommunications & Cloud Networking',
            'is_top_alumni': True,
            'description': 'Leading next-generation enterprise SD-WAN solutions and edge computing architectures across APAC region.',
            'linkedin': 'https://linkedin.com',
            'github': 'https://github.com',
            'profile_photo': profile_photos[0]
        },
        {
            'email': 'ananya.deshmukh@example.com',
            'full_name': 'Ananya Das',
            'mobile': '+91 9823456789',
            'current_job_profile': 'Senior AI/ML Research Engineer',
            'current_company': 'Google Cloud',
            'current_job_location': 'Hyderabad, India',
            'city': 'Hyderabad',
            'sub_district': 'Gachibowli',
            'district': 'Hyderabad',
            'state': 'Telangana',
            'pincode': '500032',
            'is_international': False,
            'country': 'India',
            'full_address': 'Plot 18, Financial District, Nanakramguda, Hyderabad',
            'graduation_year': 2020,
            'experience': 5,
            'sector': 'Artificial Intelligence & Signal Processing',
            'is_top_alumni': True,
            'description': 'Specializing in computer vision models for telecom sensor networks and real-time anomaly detection.',
            'linkedin': 'https://linkedin.com',
            'github': 'https://github.com',
            'profile_photo': profile_photos[1]
        },
        {
            'email': 'siddharth.patil@example.com',
            'full_name': 'Siddharth Mohanty',
            'mobile': '+1 (408) 555-0199',
            'current_job_profile': 'Principal ASIC Design Engineer',
            'current_company': 'NVIDIA Corporation',
            'current_job_location': 'Santa Clara, CA, USA',
            'city': 'Santa Clara',
            'sub_district': 'Silicon Valley',
            'district': 'Santa Clara County',
            'state': 'California',
            'pincode': '95051',
            'is_international': True,
            'country': 'United States',
            'full_address': '2788 San Tomas Expy, Santa Clara, CA 95051',
            'graduation_year': 2016,
            'experience': 9,
            'sector': 'Semiconductors & VLSI',
            'is_top_alumni': True,
            'description': 'Architecting next-gen tensor core hardware accelerators and high-speed interconnects for deep learning clusters.',
            'linkedin': 'https://linkedin.com',
            'github': 'https://github.com',
            'profile_photo': profile_photos[2]
        },
        {
            'email': 'pooja.kulkarni@example.com',
            'full_name': 'Pooja Nayak',
            'mobile': '+91 9765432109',
            'current_job_profile': 'Embedded Firmware Lead',
            'current_company': 'Qualcomm India',
            'current_job_location': 'Pune, Maharashtra',
            'city': 'Pune',
            'sub_district': 'Haveli',
            'district': 'Pune',
            'state': 'Maharashtra',
            'pincode': '411057',
            'is_international': False,
            'country': 'India',
            'full_address': 'Hinjawadi Phase 2, Pune, Maharashtra 411057',
            'graduation_year': 2021,
            'experience': 4,
            'sector': 'Wireless Embedded Systems & 5G/6G',
            'is_top_alumni': True,
            'description': 'Developing low-power modem firmware and RF physical layer drivers for Snapdragon mobile platforms.',
            'linkedin': 'https://linkedin.com',
            'github': 'https://github.com',
            'profile_photo': profile_photos[3]
        },
        {
            'email': 'aditya.joshi@example.com',
            'full_name': 'Aditya Tripathy',
            'mobile': '+91 9422113355',
            'current_job_profile': 'Engineering Manager',
            'current_company': 'Tata Consultancy Services',
            'current_job_location': 'Bhubaneswar, India',
            'city': 'Bhubaneswar',
            'sub_district': 'Infocity',
            'district': 'Khurda',
            'state': 'Odisha',
            'pincode': '751024',
            'is_international': False,
            'country': 'India',
            'full_address': 'Infocity, Patia, Bhubaneswar 751024',
            'graduation_year': 2022,
            'experience': 3,
            'sector': 'Information Technology',
            'is_top_alumni': False,
            'description': 'Managing cloud integration projects and coordinating regional PMEC alumni mentorship initiatives.',
            'linkedin': 'https://linkedin.com',
            'profile_photo': profile_photos[4]
        },
        {
            'email': 'tanvi.shinde@example.com',
            'full_name': 'Tanvi Rout',
            'mobile': '+91 9860123456',
            'current_job_profile': 'IoT Solutions Consultant',
            'current_company': 'Siemens Digital Industries',
            'current_job_location': 'Mumbai, Maharashtra',
            'city': 'Mumbai',
            'sub_district': 'Thane',
            'district': 'Thane',
            'state': 'Maharashtra',
            'pincode': '400601',
            'is_international': False,
            'country': 'India',
            'full_address': 'Airoli Knowledge Park, Navi Mumbai 400708',
            'graduation_year': 2023,
            'experience': 2,
            'sector': 'Industrial Automation & IoT',
            'is_top_alumni': False,
            'description': 'Building smart factory telemetry solutions and industrial sensor gateways.',
            'linkedin': 'https://linkedin.com',
            'profile_photo': profile_photos[5]
        }
    ]

    for item in demo_alumni_data:
        email = item.pop('email')
        alumni, created = Alumni.objects.get_or_create(
            email=email,
            defaults={
                'id': str(uuid.uuid4())[:8],
                'password': make_password('password123'),
                **item
            }
        )
        if not created:
            alumni.password = make_password('password123')
            for k, v in item.items():
                setattr(alumni, k, v)
            alumni.save()
    print(f"Seeded {len(demo_alumni_data)} alumni records (Demo login: rahul.sharma@example.com / password123)")

    # 5. Events
    event_data = [
        {
            'title': 'Grand PMEC Alumni Reunion & Homecoming Gala 2025',
            'description': 'Join us at the Parala Maharaja Engineering College Main Auditorium for a memorable evening reconnecting with classmates, faculty, and commemorating departmental excellence.',
            'date': '2025-10-18',
            'media': 'events/fareweel.jpg' if os.path.exists(os.path.join('static', 'media', 'events', 'fareweel.jpg')) else ''
        },
        {
            'title': 'National Technical Symposium & Hackathon "Telekinesis 2025"',
            'description': 'Annual flagship technical symposium featuring 24-hour IoT hackathon, paper presentations on 6G wireless communications, and industry keynote sessions.',
            'date': '2025-08-25',
            'media': ''
        },
        {
            'title': 'PMEC Alumni Mentorship & Career Guidance Masterclass',
            'description': 'Interactive webinar and live Q&A session with alumni leaders from Cisco, Google, and NVIDIA on preparing for semiconductor and software careers.',
            'date': '2025-06-10',
            'media': ''
        }
    ]

    for ev in event_data:
        Event.objects.get_or_create(
            title=ev['title'],
            defaults=ev
        )
    print(f"Seeded {len(event_data)} events.")

    # 6. Gallery Photos
    gallery_items = [
        ('Robotics & BGMI Gaming Championship', 'gallery/bgmi.jpg', 'Students competing in the annual inter-college e-sports & robotics league.'),
        ('Circuit Design & VLSI Workshop', 'gallery/circuit.jpg', 'Hands-on practical session in digital circuit simulation and FPGA programming.'),
        ('Technical Essay & Innovation Forum', 'gallery/essa.jpg', 'Department symposium presentations on emerging trends in green telecommunications.'),
        ('Logic Puzzle & Code Quest', 'gallery/puzzel.jpg', 'Inter-department algorithmic challenge organized by E&TC student council.'),
        ('National Telecommunication Quiz League', 'gallery/quiz.jpg', 'Annual quiz competition testing fundamental signal processing and communication concepts.'),
        ('Traditional Rangoli & Cultural Fest', 'gallery/rangoli.jpg', 'Vibrant cultural celebrations during the annual department social gathering.'),
        ('Hardware Sketch & Model Exhibition', 'gallery/sctch.jpg', 'Showcasing student-built IoT prototypes and embedded telemetry hardware.'),
        ('Web Development & Cloud Hackathon', 'gallery/web.jpg', 'Teams designing modern cloud-native portals and real-time dashboard applications.'),
        ('Alumni Meet Campus Felicitation', 'gallery/WhatsApp_Image_2025-04-21_at_11.37.10_8deacff6.jpg', 'Honoring distinguished alumni guests during the department felicitation ceremony.')
    ]

    for title, img_path, desc in gallery_items:
        if os.path.exists(os.path.join('static', 'media', img_path)):
            GalleryPhoto.objects.get_or_create(
                title=title,
                defaults={'image': img_path, 'description': desc}
            )
    print("Seeded gallery photos from existing static assets.")

    # 7. Visitor Count
    visitor, _ = VisitorCount.objects.get_or_create(id=1)
    if visitor.count < 150:
        visitor.count = 150
        visitor.save()

    # 8. Superuser for Django Admin
    admin_user = Alumni.objects.filter(email='admin@pmec.ac.in').first()
    if not admin_user:
        admin_user = Alumni.objects.create_superuser(
            email='admin@pmec.ac.in',
            full_name='PMEC Portal Administrator',
            password='adminpassword123',
            graduation_year=2015,
            city='Berhampur',
            district='Ganjam',
            state='Odisha',
            pincode='761003',
            full_address='PMEC Campus, Sitalapalli, Berhampur, Odisha'
        )
        print("Created superuser: admin@pmec.ac.in / adminpassword123")
    else:
        admin_user.set_password('adminpassword123')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        print("Updated superuser: admin@pmec.ac.in / adminpassword123")

    print("\nDatabase seeding completed successfully!")

if __name__ == '__main__':
    seed()
