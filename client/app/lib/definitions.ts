import { z } from "zod";

export const SignInSchema = z.object({
  username: z.string().min(3, "Username is required"),
  password: z.string().min(1, "Password is required"),
});

export type TSignInSchema = z.infer<typeof SignInSchema>;

export type FormState =
  | {
      errors?: {
        name?: string[];
        password?: string[];
      };
      message?: string;
      error?: string;
    }
  | undefined;

export enum EConsumableType {
  VEGETABLE = "VEGETABLE",
  FRUIT = "FRUIT",
  OTHER = "OTHER",
}

export enum EAcceptedType {
  ACCEPTED = "ACCEPTED",
  NOT_ACCEPTED = "NOT_ACCEPTED",
}

export enum ERoleType {
  ADMIN = "ADMIN",
  FARMER = "FARMER",
  USER = "USER",
}

export enum EBookedType {
  BOOKED = "BOOKED",
  NOT_BOKED = "NOT_BOOKED",
}

export type ConsumableType = keyof typeof EConsumableType;
export type AcceptedType = keyof typeof EAcceptedType;
export type RoleType = keyof typeof ERoleType;

export const typeClassMap = {
  FRUIT: "bg-fruit",
  VEGETABLE: "bg-vegetable",
  OTHER: "bg-other",
};

export type RequestMethodsType = "GET" | "POST" | "PUT" | "DELETE" | "PATCH";
