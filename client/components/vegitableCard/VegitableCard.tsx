import Image from 'next/image'
import { Card, CardDescription } from '../ui/card'
import { Badge } from '../ui/badge'

type Props = {
  image: string
  alt: string
}

const VegitableCard = ({ image, alt }: Props) => {
  return (
    <Card className="p-5">
      <Image src={image} alt={alt} height={100} width={100} className="mb-3" />
      <h2 className="text-lg font-bold mb-3">Name</h2>
      <Badge className="bg-slate-700 mb-3">Type of Vegitable</Badge>
      <CardDescription className=" text-sm">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean euismod
        bibendum laoreet.
      </CardDescription>
    </Card>
  )
}

export default VegitableCard
