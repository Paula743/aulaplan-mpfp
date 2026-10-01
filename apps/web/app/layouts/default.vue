<template>
  <div class="drawer lg:drawer-open min-h-screen">
    <input id="aulaplan-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex min-w-0 flex-col">
      <AppHeader />
      <main class="p-4 lg:p-6">
        <slot />
      </main>
    </div>
    <div class="drawer-side z-40">
      <label for="aulaplan-drawer" class="drawer-overlay" />
      <AppSidebar />
    </div>
  </div>
</template>