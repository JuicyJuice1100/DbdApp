import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./tabs/tabs.module').then(m => m.TabsPageModule)
  },
  {
    path: 'my-builds',
    loadChildren: () => import('./my-builds/my-builds.module').then( m => m.MyBuildsPageModule)
  },
  {
    path: 'new-build',
    loadChildren: () => import('./new-build/new-build.module').then( m => m.NewBuildPageModule)
  }
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
