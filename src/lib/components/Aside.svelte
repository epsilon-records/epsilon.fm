<script lang="ts">
	import AsideNavbarLower from './AsideNavbarLower.svelte';
	import AsideNavbarUpper from './AsideNavbarUpper.svelte';
</script>

<aside
	class="fixed inset-y-0 left-0 z-10 hidden w-14 flex-col border-r bg-background pt-10 sm:flex"
>
	<AsideNavbarUpper />
	<AsideNavbarLower />
</aside>
