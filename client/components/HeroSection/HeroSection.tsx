import React from 'react'
import Image from 'next/image'

import { IoIosLeaf } from 'react-icons/io'
import { FaArrowRight } from 'react-icons/fa'

import { Badge } from '../ui/badge'
import { Card, CardContent } from '../ui/card'
import { Button } from '../ui/button'

const HeroSection = () => {
  return (
    <div className="mx-auto w-11/12 py-3 grid grid-cols-2">
      <div>
        <Badge variant={'outline'}>
          <IoIosLeaf className="text-primary" />
          Text
        </Badge>
        <Badge variant={'outline'}>
          <IoIosLeaf className="text-primary" />
          Text
        </Badge>
        <h1 className="text-3xl mb-3">Lorem ipsum dolor sit</h1>
        <Button className="text-md">
          Start Shopping <FaArrowRight />
        </Button>
      </div>
      <div className="flex gap-3">
        <Card>
          <Image
            src={'/farm-land.jpg'}
            alt="farm land"
            width={200}
            height={200}
          />
          <CardContent></CardContent>
        </Card>
        <Card>
          <Image
            src={'/farm-land.jpg'}
            alt="farm land"
            width={200}
            height={200}
          />
          <CardContent></CardContent>
        </Card>
      </div>
    </div>
  )
}

export default HeroSection
