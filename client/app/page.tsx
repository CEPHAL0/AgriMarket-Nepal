import Image from 'next/image'
import Navbar from '../components/Navbar/Navbar'
import Footer from '@/components/Footer/Footer'
import MainLayout from '@/components/MainLayout/MainLayout'
import HeroSection from '@/components/HeroSection/HeroSection'
import Premium from '@/components/Premium/Premium'
import BestSelling from '@/components/BestSelling/BestSelling'

export default function Home() {
  return (
    <MainLayout>
      <HeroSection />
      <Premium />
      <BestSelling />
    </MainLayout>
  )
}
