<script lang="ts">
	import type { PageData } from './$types.js';
	import ProfileForm from './ProfileForm.svelte';
	export let data: PageData;
</script>

<ProfileForm data={data.form} />
