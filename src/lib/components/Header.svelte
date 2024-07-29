<script lang="ts">
	import UserSwitcher from './UserSwitcher.svelte';
	import ArtistSwitcher from './ArtistSwitcher.svelte';
	import SearchBar from './SearchBar.svelte';
	import SelectMode from './SelectMode.svelte';
	import NavbarSheet from './NavbarSheet.svelte';
	import Breadcrumbs from './Breadcrumbs.svelte';
</script>

<header
	class="sticky top-14 z-30 flex h-14 items-center gap-4 border-b bg-background px-4 sm:static sm:h-auto sm:border-0 sm:px-6"
>
	<NavbarSheet></NavbarSheet>
	<ArtistSwitcher></ArtistSwitcher>
	<Breadcrumbs></Breadcrumbs>
	<SearchBar></SearchBar>
	<SelectMode></SelectMode>
	<UserSwitcher></UserSwitcher>
</header>
