import Image from 'next/image'
import Navbar from '../components/Navbar/Navbar'
import Footer from '@/components/Footer/Footer'
import MainLayout from '@/components/MainLayout/MainLayout'
import HeroSection from '@/components/HeroSection/HeroSection'

export default function Home() {
  return (
    <MainLayout>
      <HeroSection />
      <div>Hello World</div>
    </MainLayout>
  )
}
