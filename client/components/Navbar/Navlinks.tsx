import Link from 'next/link'

const Navlinks = () => {
  const links: Link[] = [
    {
      name: 'Home',
      path: '/'
    },
    {
      name: 'About',
      path: '/about'
    },
    {
      name: 'Contact',
      path: '/contact'
    }
  ]

  return (
    <>
      {links.map((link, index) => (
        <li key={index}>
          <Link href={link.path}>{link.name}</Link>
        </li>
      ))}
    </>
  )
}

export default Navlinks
