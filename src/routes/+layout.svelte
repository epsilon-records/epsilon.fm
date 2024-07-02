<script lang="ts">
	import '../app.postcss';
	import { AppLayout, AppBar, NavItem } from 'svelte-ux';
</script>

<!-- App Shell -->
<AppLayout areas="'header header' 'aside main'">
  <svelte:fragment slot="nav">
    <!-- Nav menu -->
  </svelte:fragment>

  <AppBar title="Example">
    <div slot="actions">
      <!-- App actions -->
    </div>
  </AppBar>

  <main>
    <slot />
  </main>
</AppLayout>
