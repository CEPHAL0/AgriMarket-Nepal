import MainLayout from '@/components/MainLayout/MainLayout'
import React, { ReactNode } from 'react'

const Layout = ({ children }: { children: ReactNode }) => {
  return <MainLayout>{children}</MainLayout>
}

export default Layout
