---
name: developer-nextjs
description: Next.js full-stack development standards and best practices. Provides App Router patterns, Server Components architecture, and Next.js-specific guidelines for full-stack React applications.
---

<!-- Updated: 2025-11-11 19:15:00 UTC -->

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
