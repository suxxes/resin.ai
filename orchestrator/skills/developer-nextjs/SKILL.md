---
name: developer-nextjs
description: Next.js full-stack development standards and best practices. Provides App Router patterns, Server Components architecture, and Next.js-specific guidelines for full-stack React applications.
---

<!-- Updated: 2025-11-11 19:00:00 UTC -->

# Next.js Development Skill

This skill provides Next.js-specific standards and best practices for full-stack development with the App Router and Server Components.

## NEXT.JS STANDARDS

### Server Components First
- **Default to RSC**: Use Server Components unless client interactivity needed
- **Data Fetching**: Fetch data in Server Components (async components)
- **Database Access**: Query databases directly in Server Components
- **Streaming**: Use Suspense boundaries for progressive rendering
- **Client Boundary**: Mark Client Components with 'use client' directive only when needed
- **Minimize Client JS**: Keep client bundle size small

### Code Organization
- **App Router**: Use `app/` directory structure
- **Route Groups**: Organize with `(group-name)/` for logical grouping without affecting URL
- **Co-location**: Keep components, styles, and tests near their routes
- **Server vs Client**: Separate server and client logic clearly
- **Special Files**: Use `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`, `route.ts`

### Performance Optimization
- **Image Optimization**: Use `next/image` for all images with proper width/height
- **Font Optimization**: Use `next/font` for web fonts
- **Link Prefetching**: Use `next/link` for navigation
- **Dynamic Imports**: Code split Client Components with `next/dynamic`
- **Metadata**: Use `generateMetadata` for dynamic SEO

### Security Standards
- **Environment Variables**: Use `NEXT_PUBLIC_` prefix ONLY for client-exposed variables
- **Server Actions**: Validate all inputs, use revalidatePath/revalidateTag appropriately
- **API Security**: Validate and sanitize all inputs in route handlers

### Best Practices
- **Error Boundaries**: Implement `error.tsx` files at appropriate route levels
- **Loading States**: Add `loading.tsx` files for Suspense boundaries
- **Layouts**: Use `layout.tsx` for shared UI across routes
- **Server Actions**: Prefer server actions over API routes for mutations
- **Parallel Routes**: Use `@folder` for simultaneous rendering when needed
- **TypeScript**: Type all props, server actions, and route handlers

## NEXT.JS PATTERNS

### Server Component (Async Data Fetching)
```typescript
// app/users/page.tsx
export default async function UsersPage() {
  const users = await db.user.findMany();
  return <UserList users={users} />;
}
```

### Client Component (Interactivity)
```typescript
// components/Counter.tsx
'use client';

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

### Server Actions
```typescript
// app/actions.ts
'use server';

import { revalidatePath } from 'next/cache';

export async function updateUser(formData: FormData) {
  const name = formData.get('name') as string;
  await db.user.update({ where: { id: 1 }, data: { name } });
  revalidatePath('/users');
}
```

### API Route Handler
```typescript
// app/api/users/route.ts
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const users = await db.user.findMany();
  return NextResponse.json(users);
}

export async function POST(request: Request) {
  const body = await request.json();
  const user = await db.user.create({ data: body });
  return NextResponse.json(user);
}
```

### Dynamic Metadata
```typescript
// app/users/[id]/page.tsx
import { Metadata } from 'next';

export async function generateMetadata({ params }: { params: { id: string } }): Promise<Metadata> {
  const user = await db.user.findUnique({ where: { id: params.id } });
  return { title: user.name };
}
```

### Loading and Error States
```typescript
// app/users/loading.tsx
export default function Loading() {
  return <div>Loading users...</div>;
}

// app/users/error.tsx
'use client';

export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

### Environment Variables
```bash
# .env.local
DATABASE_URL=postgres://...           # Server-only
NEXT_PUBLIC_API_URL=https://api.com   # Client-accessible
```

```typescript
// Access in server components/actions
process.env.DATABASE_URL

// Access in client components (must have NEXT_PUBLIC_ prefix)
process.env.NEXT_PUBLIC_API_URL
```
