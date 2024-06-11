import React from 'react'

const BestSelling = () => {
  return (
    <div className="mx-auto w-11/12 bg-[#6d8434] m-2 p-5 rounded-lg text-white">
      <h5 className="uppercase text-base font-bold mb-4">
        <span className="text-red-500 ">||</span> Best Selling
      </h5>
      <div className="flex gap-10">
        <h2 className="text-2xl font-semibold flex-grow">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur,
          quam. Veniam fuga sapiente autem tempore
        </h2>
        <h4 className="text-lg flex-grow-0 w-1/3">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Molestias
          numquam non reprehenderit libero iusto voluptatum
        </h4>
      </div>
    </div>
  )
}

export default BestSelling
