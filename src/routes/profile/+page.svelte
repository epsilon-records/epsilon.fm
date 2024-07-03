<script lang="ts">
	import type { PageData } from './$types.js';
	import ProfileForm from './profile-form.svelte';
	export let data: PageData;
</script>

<ProfileForm data={data.form} />
