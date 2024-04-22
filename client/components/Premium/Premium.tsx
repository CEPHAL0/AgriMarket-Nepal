import React from 'react'
import { Card, CardContent } from '../ui/card'
import { Badge } from '../ui/badge'
import Image from 'next/image'

const Premium = () => {
  return (
    <div className="bg-[#6d8434] p-5">
      <div className="w-11/12 mx-auto grid grid-cols-3 gap-8">
        <Card
          className="text-white border-0 p-5"
          style={{
            background:
              "url('https://images.unsplash.com/photo-1518977676601-b53f82aba655?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')",
            backgroundSize: 'cover',
            height: '200px',
            width: '500px'
          }}
        >
          <CardContent>
            <Badge variant={'outline'} className="text-white text-base px-3">
              Premium
            </Badge>
            <p>small potatos</p>
            <h5>Vegetables</h5>
            <p>price here</p>
          </CardContent>
        </Card>
        <h3 className="text-3xl text-white">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae
        </h3>
        <Image
          src={'/tractor.jpg'}
          alt="tractor"
          width={300}
          height={300}
          className="ml-5"
        />
      </div>
    </div>
  )
}

export default Premium
