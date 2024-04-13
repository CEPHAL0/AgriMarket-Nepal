import Image from 'next/image'
import { CiSearch } from 'react-icons/ci'
import Navlinks from './Navlinks'

const Navbar = () => {
  return (
    <div className="border-b-2 w-full">
      <div className="w-11/12 mx-auto  flex items-center justify-around py-2 ">
        <Image src={'/logo.jpeg'} alt="logo" width={80} height={80} />
        <ul className="flex gap-3 ">
          <Navlinks />
        </ul>
        <CiSearch className="text-2xl " />
      </div>
    </div>
  )
}

export default Navbar
