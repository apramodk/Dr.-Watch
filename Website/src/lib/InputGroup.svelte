<script>
	import { Input, Label } from 'flowbite-svelte';
	export let inputName = 'default-input';
</script>

<div>
	<Label for="default-input" class="block mb-2">{inputName}</Label>
	<Input id="default-input" class={inputName} placeholder={inputName} />
</div>
