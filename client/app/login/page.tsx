"use client";

import LoginForm from "@/components/Login/LoginForm";
import Image from "next/image";
import Vegetable from "@/public/Vegetables.jpg";

const Login = () => {
  return (
    <div className="flex min-h-full h-screen justify-center bg-primary-gray p-6">
      <div className="grow flex flex-col  gap-4 items-center justify-center">
        <p className="text-2xl font-bold text-primary-blue">Login</p>
        <LoginForm />
      </div>
      <div className="w-[40%] relative sm:block hidden">
        <Image
          src={Vegetable}
          alt="Vegetable"
          fill
          className="rounded-xl object-cover"
        />
      </div>
    </div>
  );
};

export default Login;
