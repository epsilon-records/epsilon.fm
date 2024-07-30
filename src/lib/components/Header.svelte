<script lang="ts">
	import UserSwitcher from './UserSwitcher.svelte';
	import ArtistSwitcher from './ArtistSwitcher.svelte';
	import SearchBar from './SearchBar.svelte';
	import SelectMode from './SelectMode.svelte';
	import NavbarSheet from './NavbarSheet.svelte';
	import Breadcrumbs from './Breadcrumbs.svelte';
</script>

<header
	class="sticky top-8 z-30 flex h-14 items-center gap-4 border-b border-t bg-background px-4 sm:px-6"
>
	<NavbarSheet />
	<ArtistSwitcher />
	<Breadcrumbs />
	<SearchBar />
	<SelectMode />
	<UserSwitcher />
</header>
