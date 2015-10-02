# Graphics and Animation

**Topics**

- 2D Graphics
  - [ImageView](http://developer.android.com/reference/android/widget/ImageView.html)
  - [Canvas](http://developer.android.com/guide/topics/graphics/2d-graphics.html)
- [View Animation](http://developer.android.com/guide/topics/graphics/view-animation.html)
- [Property Animation](http://developer.android.com/guide/topics/graphics/prop-animation.html)

## 2D Graphics

Draw to a view when:

- Simple graphics
- Little or no updates

Draw to a canvas when:

- Complex graphics
- Regular updates

The [Drawable](http://developer.android.com/reference/android/graphics/drawable/Drawable.html) class represents things that can be drawn. For e.g. bitmaps, colors, shapes etc.

- [BitmapDrawable](http://developer.android.com/reference/android/graphics/drawable/BitmapDrawable.html)
- [ColorDrawable](http://developer.android.com/reference/android/graphics/drawable/ColorDrawable.html)
- [ShapeDrawable](http://developer.android.com/reference/android/graphics/drawable/ShapeDrawable.html)

Drawing with a canvas, you will need:

- A bitmap (a matrix of pixels)
- A canvas for drawing to the underlying bitmap
- A drawing primitive (e.g. rectangle, text, path, bitmap, etc.)
- A paint object (for setting drawing colors and styles)

A surface view provides a dedicated drawing surface embedded inside of a view hierarchy.

- [SurfaceView](http://developer.android.com/reference/android/view/SurfaceView.html)

## View Animation

- [View Animation](http://developer.android.com/guide/topics/graphics/view-animation.html)
- [TransitionDrawable](http://developer.android.com/reference/android/graphics/drawable/TransitionDrawable.html)
- [AnimationDrawable](http://developer.android.com/reference/android/graphics/drawable/AnimationDrawable.html)
- [Animation](http://developer.android.com/reference/android/view/animation/Animation.html)

## Property Animation

- [Property Animation](http://developer.android.com/guide/topics/graphics/prop-animation.html)

**Resources**

- [Building Apps with Graphics and Animation](http://developer.android.com/training/building-graphics.html)
- [Animation and Graphics](http://developer.android.com/guide/topics/graphics/index.html)
- [Canvas and Drawables](http://developer.android.com/guide/topics/graphics/2d-graphics.html)
- [Animation Resources](http://developer.android.com/guide/topics/resources/animation-resource.html)