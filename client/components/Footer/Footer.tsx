import React from 'react'

const Footer = () => {
  return (
    <footer className="bg-black w-full">
      <div className="w-11/12 mx-auto flex justify-between py-5">
        <div>
          <h1 className="text-white">About Us</h1>
          <p className="text-white">
            We are a team of college students working on this project like
            it&apos;s our full time job. Any amount would help support and
            continue development on this project and is greatly appreciated.
          </p>
        </div>
        <div>
          <h1 className="text-white">Contact Us</h1>
          <p className="text-white">Email: test@gmail.com</p>
          <p className="text-white">Phone: 9811222333</p>
        </div>
      </div>
    </footer>
  )
}

export default Footer
