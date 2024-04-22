import VegitableCard from '@/components/vegitableCard/VegitableCard'
import React from 'react'


type Consumable = {
  consumable_id: number
  user_id: number
  price: number
  district_id: number
  quantity: number
  id: number
  created_at: string
  updated_at: string
}

type Consuables = Consumable[]

const Consuables = async () => {
  const data: Consuables = await getServerSideProps()
  return (
    <div className="w-11/12 mx-auto">
      <div className="grid grid-cols-4 gap-3 p-5">
        {/* {data.map((item) => (
          <VegitableCard
            key={item.id}
            image={item.image_path}
            alt={item.name}
          />
        ))} */}
        <VegitableCard image="/vegitable.webp" alt="vegitable" />
        <VegitableCard image="/vegitable.webp" alt="vegitable" />
        <VegitableCard image="/vegitable.webp" alt="vegitable" />
        <VegitableCard image="/vegitable.webp" alt="vegitable" />
        <VegitableCard image="/vegitable.webp" alt="vegitable" />
      </div>
    </div>
  )
}

async function getServerSideProps() {
  const res = await fetch(process.env.API_URL + '/consumableLisitings', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHBpcmUiOiIyMDI0LTA0LTIxIDIyOjM0OjIwIn0.imtzlwIRtk5YSqVTG6aHznmcRpM0WWy6rvIbQQLrgJU`
    }
  })
  if (!res.ok) {
    throw new Error('Something went wrong')
  }
  return res.json()
}

export default Consuables
