import MainLayout from "@/components/MainLayout/MainLayout";

type Props = { children: React.ReactNode };

export default function Layout({ children }: Props) {
  return <MainLayout>{children}</MainLayout>;
}
