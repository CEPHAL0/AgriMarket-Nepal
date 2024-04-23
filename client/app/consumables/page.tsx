import VegitableCard from '@/components/vegitableCard/VegitableCard'
import React from 'react'
import { fetchWithSessionId } from '../utils/fetchWithSessionId'

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
  const res = await fetchWithSessionId('/consumableLisitings', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  const data = await res.json()
  if (!res.ok) {
    // console.log(data.message)

    throw new Error(data.message)
  }
  return data
}

export default Consuables
